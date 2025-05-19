import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1747655329725 = glueContext.create_dynamic_frame.from_catalog(database="de_youtube_cleaned", table_name="cleaned_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1747655329725")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1747655351492 = glueContext.create_dynamic_frame.from_catalog(database="de_youtube_cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1747655351492")

# Script generated for node Join
Join_node1747655386171 = Join.apply(frame1=AWSGlueDataCatalog_node1747655351492, frame2=AWSGlueDataCatalog_node1747655329725, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1747655386171")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1747655386171, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1747655250676", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1747655513304 = glueContext.getSink(path="s3://de-project-youtube-analytics-useast1-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1747655513304")
AmazonS3_node1747655513304.setCatalogInfo(catalogDatabase="de_youtube_analytics",catalogTableName="final-analytics ")
AmazonS3_node1747655513304.setFormat("glueparquet", compression="snappy")
AmazonS3_node1747655513304.writeFrame(Join_node1747655386171)
job.commit()