# This is a sample Python script.

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from utils import connectionOptions
import jdbcReader
import jdbcWriter
import getConfigParser


if __name__ == '__main__':
	args = getResolvedOptions(sys.argv, ['JOB_NAME'])

	sc = SparkContext()
	glueContext = GlueContext(sc)
	spark = glueContext.spark_session
	job = Job(glueContext)
	configPath = args[0]
	# get the config object
	configParser = getConfigParser(configPath)
	sourceDetails = configParser.sourceDetails()
	targetDetails = configParser.targetDetails()
	readConnOptions = configParser.getConnectionOptions(sourceDetails)
	writeConnOptions = configParser.getConnectionOptions(targetDetails)
	connection_options = connectionOptions(configParser.sourceType, readConnOptions)
	# conn = connectionManager.getConnection(connType, configParser)
	# glueReader = conn.getReader(glueContext)
	# sourceDF = glueReader.read(conn)
	glueReader = jdbcReader(glueContext)
	# read source data
	df = glueReader.glueRead(readConnOptions, configParser.sourceType)

	# write data to target
	glueWriter = jdbcWriter(glueContext)
	glueWriter.glueWrite(df, writeConnOptions, configParser.targetType)