from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, col, array_contains

# Create a SparkSession
spark = SparkSession.builder.appName('The Twitter Grab 2019 Corpus').getOrCreate()

# Set the S3 bucket and folder paths
source_bucket = 'gelctweets'
year = '2019'
month = '01'
data_source = 's3://' + source_bucket + '/' + year + '_' + month + '/*/*/*/*.json'
#data_source = 's3://' + source_bucket + '/' + year + '_' + month + '/01/00/29.json.bz2/*.json'

# Read the JSONL files into a DataFrame
tweets_spark_df = spark.read.json(data_source)

# Define the list of hashtags for DataFrame filtering
hashtags = [
    'chavista', 
    'Chavista', 
    'CHAVISTA', 
    'fueravenecos', 
    'Fueravenecos', 
    'FueraVenecos', 
    'FUERAVENECOS', 
    'migrantevenezolano', 
    'Migrantevenezolano', 
    'MigranteVenezolano', 
    'MIGRANTEVENEZOLANO', 
    'portugalvenezuela', 
    'Portugalvenezuela', 
    'PortugalVenezuela', 
    'PORTUGALVENEZUELA', 
    'prayforvenezuela', 
    'Prayforvenezuela', 
    'PrayForVenezuela', 
    'PRAYFORVENEZUELA', 
    'refugiadovenezolano', 
    'Refugiadovenezolano', 
    'RefugiadoVenezolano', 
    'REFUGIADOVENEZOLANO', 
    'transperuzolano', 
    'Transperuzolano', 
    'TRANSPERUZOLANO', 
    'veneca', 
    'Veneca', 
    'VENECA', 
    'veneco', 
    'Veneco', 
    'VENECO', 
    'venecobardes', 
    'Venecobardes', 
    'VENECOBARDES', 
    'venezolana', 
    'Venezolana', 
    'VENEZOLANA', 
    'venezolandia', 
    'Venezolandia', 
    'VENEZOLANDIA', 
    'venezolano', 
    'Venezolano', 
    'VENEZOLANO', 
    'venezolanodemierda', 
    'Venezolanodemierda', 
    'VenezolanoDeMierda', 
    'VENEZOLANODEMIERDA', 
    'venezolanoshijosdeputa', 
    'Venezolanoshijosdeputa', 
    'VenezolanosHijosDePuta', 
    'VENEZOLANOSHIJOSDEPUTA', 
    'venezuela', 
    'Venezuela', 
    'VENEZUELA', 
    'venezuelaenlacalle', 
    'Venezuelaenlacalle', 
    'VenezuelaEnLaCalle', 
    'VENEZUELAENLACALLE', 
    'venezuelazo', 
    'Venezuelazo', 
    'VENEZUELAZO', 
    'venezuelazuela', 
    'Venezuelazuela'
]

expressions = [
    'caraqueño', 
    'chaveta veneco', 
    'criollo veneco', 
    'guarimbeiros', 
    'parasitos venezolanos', 
    'refugiados de la miseria venezuela', 
    'sudaca venezolano', 
    'venecao', 
    'veneccio', 
    'venepobre', 
    'veneputas'
]

# Create a filtered DataFrame
filtered_tweets_spark_df = tweets_spark_df.filter(
    array_contains('entities.hashtags.text', hashtags[0]) |\
    array_contains('entities.hashtags.text', hashtags[1]) |\
    array_contains('entities.hashtags.text', hashtags[2]) |\
    array_contains('entities.hashtags.text', hashtags[3]) |\
    array_contains('entities.hashtags.text', hashtags[4]) |\
    array_contains('entities.hashtags.text', hashtags[5]) |\
    array_contains('entities.hashtags.text', hashtags[6]) |\
    array_contains('entities.hashtags.text', hashtags[7]) |\
    array_contains('entities.hashtags.text', hashtags[8]) |\
    array_contains('entities.hashtags.text', hashtags[9]) |\
    array_contains('entities.hashtags.text', hashtags[10]) |\
    array_contains('entities.hashtags.text', hashtags[11]) |\
    array_contains('entities.hashtags.text', hashtags[12]) |\
    array_contains('entities.hashtags.text', hashtags[13]) |\
    array_contains('entities.hashtags.text', hashtags[14]) |\
    array_contains('entities.hashtags.text', hashtags[15]) |\
    array_contains('entities.hashtags.text', hashtags[16]) |\
    array_contains('entities.hashtags.text', hashtags[17]) |\
    array_contains('entities.hashtags.text', hashtags[18]) |\
    array_contains('entities.hashtags.text', hashtags[19]) |\
    array_contains('entities.hashtags.text', hashtags[20]) |\
    array_contains('entities.hashtags.text', hashtags[21]) |\
    array_contains('entities.hashtags.text', hashtags[22]) |\
    array_contains('entities.hashtags.text', hashtags[23]) |\
    array_contains('entities.hashtags.text', hashtags[24]) |\
    array_contains('entities.hashtags.text', hashtags[25]) |\
    array_contains('entities.hashtags.text', hashtags[26]) |\
    array_contains('entities.hashtags.text', hashtags[27]) |\
    array_contains('entities.hashtags.text', hashtags[28]) |\
    array_contains('entities.hashtags.text', hashtags[29]) |\
    array_contains('entities.hashtags.text', hashtags[30]) |\
    array_contains('entities.hashtags.text', hashtags[31]) |\
    array_contains('entities.hashtags.text', hashtags[32]) |\
    array_contains('entities.hashtags.text', hashtags[33]) |\
    array_contains('entities.hashtags.text', hashtags[34]) |\
    array_contains('entities.hashtags.text', hashtags[35]) |\
    array_contains('entities.hashtags.text', hashtags[36]) |\
    array_contains('entities.hashtags.text', hashtags[37]) |\
    array_contains('entities.hashtags.text', hashtags[38]) |\
    array_contains('entities.hashtags.text', hashtags[39]) |\
    array_contains('entities.hashtags.text', hashtags[40]) |\
    array_contains('entities.hashtags.text', hashtags[41]) |\
    array_contains('entities.hashtags.text', hashtags[42]) |\
    array_contains('entities.hashtags.text', hashtags[43]) |\
    array_contains('entities.hashtags.text', hashtags[44]) |\
    array_contains('entities.hashtags.text', hashtags[45]) |\
    array_contains('entities.hashtags.text', hashtags[46]) |\
    array_contains('entities.hashtags.text', hashtags[47]) |\
    array_contains('entities.hashtags.text', hashtags[48]) |\
    array_contains('entities.hashtags.text', hashtags[49]) |\
    array_contains('entities.hashtags.text', hashtags[50]) |\
    array_contains('entities.hashtags.text', hashtags[51]) |\
    array_contains('entities.hashtags.text', hashtags[52]) |\
    array_contains('entities.hashtags.text', hashtags[53]) |\
    array_contains('entities.hashtags.text', hashtags[54]) |\
    array_contains('entities.hashtags.text', hashtags[55]) |\
    array_contains('entities.hashtags.text', hashtags[56]) |\
    array_contains('entities.hashtags.text', hashtags[57]) |\
    array_contains('entities.hashtags.text', hashtags[58]) |\
    array_contains('entities.hashtags.text', hashtags[59]) |\
    array_contains('entities.hashtags.text', hashtags[60]) |\
    array_contains('entities.hashtags.text', hashtags[61]) |\
    array_contains('entities.hashtags.text', hashtags[62]) |\
    array_contains('entities.hashtags.text', hashtags[63]) |\
    lower(col('text')).contains(expressions[0]) |\
    lower(col('text')).contains(expressions[1]) |\
    lower(col('text')).contains(expressions[2]) |\
    lower(col('text')).contains(expressions[3]) |\
    lower(col('text')).contains(expressions[4]) |\
    lower(col('text')).contains(expressions[5]) |\
    lower(col('text')).contains(expressions[6]) |\
    lower(col('text')).contains(expressions[7]) |\
    lower(col('text')).contains(expressions[8]) |\
    lower(col('text')).contains(expressions[9]) |\
    lower(col('text')).contains(expressions[10])
)

# Export the DataFrame to JSONL format
#output_path = 's3://gelcawsemr/2019_01_01_00/filtered_tweets.jsonl'
output_path = 's3://gelcawsemr/2019_01/filtered_tweets.jsonl'
filtered_tweets_spark_df.write.mode('overwrite').json(output_path)
