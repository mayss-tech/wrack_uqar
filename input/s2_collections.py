import ee



# --- Dates ---
START = '2019-01-01'
END = '2024-12-31'

# --- Collections sources ---
S2 = (
    ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterDate(START, END)
    .filterBounds()
)

S2c = (
    ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
    .filterDate(START, END)
    .filterBounds()
)

# --- Joindre les 2 collections --- 
join = ee.Join.saveBest(
    matchKey='cloud_prob',
    measureKey='time_diff'
)

condition = ee.Filter.maxDifference(
    difference=1000 * 60 * 60,  # 1 heure
    leftField='system:time_start',
    rightField='system:time_start'
)

S2_joined = ee.ImageCollection(
    join.apply(S2, S2c, condition)
)





print("S2 SR :", S2.size().getInfo())
print("S2 Cloud Probability :", S2c.size().getInfo())
print("S2 joint :", S2_joined.size().getInfo())
