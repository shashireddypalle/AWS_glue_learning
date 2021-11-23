class connectionOptions():

     def __init__(self, connectionType, connectionOptions):

         if connectionType == 'oracle':
              # Construct JDBC connection options
              connection_options = {
                   "url" : connectionOptions['url'],
                   "dbtable" : connectionOptions['dbtable'],
                   "driver" : connectionOptions['driver'],
                   "user" : connectionOptions['user'],
                   "password" : connectionOptions['password'],
              }

         if connectionType == "documentdb":
              # Construct JDBC connection options
              connection_options = {
                   "uri": connectionOptions['url'],
                   "database": "test",
                   "collection": "coll",
                   "username": "username",
                   "password": "1234567890",
                   "ssl": "true",
                   "ssl.domain_match": "false",
                   "partitioner": "MongoSamplePartitioner",
                   "partitionerOptions.partitionSizeMB": "10",
                   "partitionerOptions.partitionKey": "_id"
              }

              # connection_mysql5_options = {
              #      "url": "jdbc:mysql://<jdbc-host-name>:3306/db",
              #      "dbtable": "test",
              #      "user": "admin",
              #      "password": "pwd"}
              #
              # connection_mysql8_options = {
              #      "url": "jdbc:mysql://<jdbc-host-name>:3306/db",
              #      "dbtable": "test",
              #      "user": "admin",
              #      "password": "pwd",
              #      "customJdbcDriverS3Path": "s3://path/mysql-connector-java-8.0.17.jar",
              #      "customJdbcDriverClassName": "com.mysql.cj.jdbc.Driver"}
              #
              # connection_oracle11_options = {
              #      "url": "jdbc:oracle:thin:@//<jdbc-host-name>:1521/ORCL",
              #      "dbtable": "test",
              #      "user": "admin",
              #      "password": "pwd"}
              #
              # connection_oracle18_options = {
              #      "url": "jdbc:oracle:thin:@//<jdbc-host-name>:1521/ORCL",
              #      "dbtable": "test",
              #      "user": "admin",
              #      "password": "pwd",
              #      "customJdbcDriverS3Path": "s3://path/ojdbc10.jar",
              #      "customJdbcDriverClassName": "oracle.jdbc.OracleDriver"}


         return connection_options
