from utils import connectionOptions
class jdbcWriter():

    def __init__(self, glue_context):
        self._glue_context = glue_context

    def glueWrite(self, df, connectionOptions, targetType):
        self._df = df
        self._dbtype = targetType
        self._connOptions = connectionOptions(self._dbtype)
        # JDBC glue writer
        status = self._glueContext.write_from_options(frame_or_dfc=self._df, connection_type=self._dbtype, connection_options=self._connOptions)

        return status