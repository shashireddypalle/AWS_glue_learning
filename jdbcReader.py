from utils import connectionOptions
class jdbcReader():

    def __init__(self, glue_context):
        self._glue_context = glue_context

    def glueRead(self, connectionOptions, sourceType):
        self._connOptions = connectionOptions(self._dbtype)
        self._dbtype = sourceType
        dataframe = self._glue_context.create_dynamic_frame.from_options(connection_type=self._dbtype,  connection_options=self._connOptions)

        return dataframe
