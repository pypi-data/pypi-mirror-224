import io
import sys
from azure.storage.blob import BlobClient, BlobServiceClient, BlobProperties
from typing import Final
from pypomes_core import APP_PREFIX, env_get_str, exc_format

# connection string to Azure
AZURE_CONNECTION_STRING: Final[str] = env_get_str(f"{APP_PREFIX}_AZURE_CONNECTION_STRING")

#  storage bucket name
AZURE_STORAGE_BUCKET: Final[str] = env_get_str(f"{APP_PREFIX}_AZURE_STORAGE_BUCKET")


def azure_verify(errors: list[str]) -> bool:
    """
    Verify whether a connection to the Azure cloud services is possible.

    :param errors: incidental errors
    :return: True if a connection is possible, or False otherwise
    """
    # initialize the return variable
    result: bool = False

    try:
        client: BlobServiceClient = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        client.close()
        result = True
    except Exception as e:
        errors.append(__azure_except_msg(e))

    return result


def azure_blob_exists(errors: list[str], blob_path: str,
                      bucket_name: str = AZURE_STORAGE_BUCKET) -> bool:
    """
    Verify whether the file referred to by *blob_path*, within *bucket_name*, exists.

    :param errors: incidental errors
    :param blob_path: file path within the bucket
    :param bucket_name: name of bucket (defaults to AZURE_STORAGE_BUCKET)
    :return: True if the file exists, False otherwise, or None in case of error
    """
    # initialize the return variable
    result: bool | None = None

    try:
        with BlobClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING,
            container_name=bucket_name,
            blob_name=blob_path
        ) as client:
            result = client.exists()
    except Exception as e:
        errors.append(__azure_except_msg(e))

    return result


def azure_blob_retrieve(errors: list[str], blob_path: str,
                        bucket_name: str = AZURE_STORAGE_BUCKET) -> bytes:
    """
    Obtem e retorna o conteúdo *raw* do arquivo apontado por *blob_path*, dentro de *bucket_name*.

    :param errors: incidental errors
    :param blob_path: caminho do arquivo no bucket
    :param bucket_name: o nome do bucket (AZURE_STORAGE_BUCKET, se não especificado)
    :return: o conteúdo do blob, ou None se houve erro
    """
    # initialize the return variable
    result: bytes | None = None

    try:
        with BlobClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING,
            container_name=bucket_name,
            blob_name=blob_path
        ) as client:
            stream: io.BytesIO = io.BytesIO()
            client.download_blob().readinto(stream)
            stream.seek(0)
            result = stream.read()
    except Exception as e:
        errors.append(__azure_except_msg(e))

    return result


def azure_blob_store(errors: list[str], content: bytes, blob_path: str,
                     bucket_name: str = AZURE_STORAGE_BUCKET) -> bool:
    """
    Armazena o conteúdo *content* no caminho apontado por *blob_path*, dentro de *bucket_name*.

    :param errors: incidental errors
    :param content: conteúdo a ser armazenado
    :param blob_path: caminho do arquivo no bucket
    :param bucket_name: o nome do bucket (AZURE_STORAGE_BUCKET, se não especificado)
    :return: True se a operação foi bem sucedida, ou False em caso contrário
    """
    # declare the return variable
    result: bool

    try:
        with BlobClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING,
            container_name=bucket_name,
            blob_name=blob_path
        ) as client:
            stream: io.BytesIO = io.BytesIO(content)
            stream.seek(0)
            client.upload_blob(data=stream,
                               blob_type="BlockBlob",
                               length=len(content),
                               overwrite=True)
            result = True
    except Exception as e:
        result = False
        errors.append(__azure_except_msg(e))

    return result


def azure_blob_delete(errors: list[str], blob_path: str,
                      bucket_name: str = AZURE_STORAGE_BUCKET) -> bool:
    """
    Remove o arquivo apontado por *blob_path*, dentro de *bucket_name*, e todos os seus *snapshots*.

    :param errors: incidental errors
    :param blob_path: caminho do arquivo no bucket
    :param bucket_name: o nome do bucket (AZURE_STORAGE_BUCKET, se não especificado)
    :return: True se a operação foi bem sucedida, ou False em caso contrário
    """
    # declare the return variable
    result: bool

    try:
        with BlobClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING,
            container_name=bucket_name,
            blob_name=blob_path
        ) as client:
            client.delete_blob(delete_snapshots="include")
            result = True
    except Exception as e:
        result = False
        errors.append(__azure_except_msg(e))

    return result


def azure_blob_get_mimetype(errors: list[str], blob_path: str,
                            bucket_name: str = AZURE_STORAGE_BUCKET) -> str:
    """
    Obtem e retorna o texxto contido no documento apontado por *file_path*, dentro de  *bucket_name*.

    Esse documento deve ser do tipo HTML ou PDF.

    :param errors: incidental errors
    :param blob_path: caminho do arquivo no bucket
    :param bucket_name: o nome do bucket (AZURE_STORAGE_BUCKET, se não especificado)
    :return: o texto do blob, codificado em UTF-8
    """
    # initialize the return variable
    result: str | None = None

    try:
        with BlobClient.from_connection_string(
            conn_str=AZURE_CONNECTION_STRING,
            container_name=bucket_name,
            blob_name=blob_path
        ) as client:
            props: BlobProperties = client.get_blob_properties()
            result = props.get("content_settings").get("content_type")
    except Exception as e:
        errors.append(__azure_except_msg(e))

    return result


def __azure_except_msg(exception: Exception) -> str:
    """
    Formata e retorna a mensagem de erro correspondente à exceção levantada no acesso ao Azure.

    :param exception: A exceção levantada
    :return: A mensagem de erro formatada
    """
    # TODO
    return exc_format(exception, sys.exc_info())


# test Azure operations
if __name__ == "__main__":

    # ruff: noqa: S101

    def __print_errors(errors: list[str], op: str) -> None:
        if len(errors) > 0:
            print(f"\nErrors in '{op}':")
            for error in errors:
                print(error)

    errors: list[str] = []
    content: bytes = b"This is the content of a sample text file."
    file_path: str = "/temp/sample.txt"

    # verify if file exists
    exists: bool = azure_blob_exists(errors, file_path)
    __print_errors(errors, "blob_exists")
    assert exists is not None, "Failed verifying file"

    # store file
    if not exists:
        success = azure_blob_store(errors, content, file_path)
        __print_errors(errors, "blob_store")
        assert success, "Failed storing file"

    # retrieve file type
    mimetype: str = azure_blob_get_mimetype(errors, file_path)
    __print_errors(errors, "blob_get_mimetype")
    assert mimetype is not None, "Failed retrieving file mimetype"

    # retrieve file contents
    retrieved: bytes = azure_blob_retrieve(errors, file_path)
    __print_errors(errors, "blob_retrieve")
    assert retrieved is not None, "Failed retrieving file content"
    print(f"Conteudo recuperado: {content}")

    # remove the file
    success = azure_blob_delete(errors, file_path)
    __print_errors(errors, "blob_delete")
    assert success, "Failed Deleting file"
