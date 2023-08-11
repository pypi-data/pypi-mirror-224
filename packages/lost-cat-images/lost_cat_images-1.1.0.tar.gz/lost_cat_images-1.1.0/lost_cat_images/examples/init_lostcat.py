from datetime import datetime
import logging
import json
import os

from sqlalchemy.engine import URL, create_engine

from lost_cat.lost_cat import LostCat
from lost_cat.processors.filesystem_scanner import FileScanner

logger = logging.getLogger(__name__)

def main():
    """Initialize and create the SQL database"""

    configpath = os.path.join("config", "security.json")
    with open(configpath, "r") as fp:
        config = json.load(fp)
        
    dbconfg = config.get("database",{})

    connection_url = URL.create(
        "mssql+pyodbc",
        username=dbconfg.get("uid"),
        password=dbconfg.get("pwd"),
        host=dbconfg.get("server"),
        database=dbconfg.get("database"),
        query={
            "driver": "ODBC Driver 17 for SQL Server",
            "autocommit": "True",
            "LongAsMax": "Yes",        
        },
    )
    logger.info("Conn: %s", connection_url)

    #engine = create_engine(connection_url)
    _paths = {
        "database": connection_url
    }
    lc = LostCat(paths=_paths)

    _src_proc = "filescanner 0.0.2"
    _uris = [
        os.path.expandvars(os.path.join("F:\\", *["source"])),
    ]

    logger.info("Paths:")
    _src_uris = []
    for _uri in _uris:
        if os.path.exists(_uri):
            _src_uris.append({
                "processor": _src_proc,
                "uri": _uri
            })
            logger.info("\t%s", _uri)
        else:
            logger.info("\t** Missing: %s", _uri)

    lc.add_processor(label= "FileSystemProcessor", 
            base_class=FileScanner
        )

    lc.load_db_sources()

    # add the sources
    for _src in _src_uris:
        try:
            lc.add_source(processor=_src.get("processor"), uri=_src.get("uri"), isroot=True, overwrite=True)
        except Exception as ex:
            logger.error("Add Source Failed: %s\n\t\t%s", _src.get("processor"), _src.get("uri"))

    lc.load_processors()

    # scan the files found...
    lc.catalog_artifacts()

    lc = None

if __name__ == "__main__":
    nb_name = "LostCat"
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists(r"data\eng\crops"):
        os.makedirs(r"data\eng\crops")

    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
    logpath = os.path.join("logs", f"{_logname}.log")
    if os.path.exists(logpath):
        os.remove(logpath)

    logging.basicConfig(filename=logpath, level=logging.INFO)

    if not os.path.exists(r"data\eng\crops"):
        os.makedirs(r"data\eng\crops")

    main()
