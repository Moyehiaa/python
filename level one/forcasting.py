# forcasting methods in python

data = [310, 365, 395, 415, 450, 465]
lenth = len(data)

# ===========================================
# calculate the summition of a list
# ===========================================

def summition (value):
    sum = 0
    for i in value :
        sum += i
    return sum

# ============================================
# Naive Forecast Method
# Uses last period’s actual value as a forecast
# ===========================================

def naive_forcast(data):
    return data[-1]

# ============================================

# MEAN (SIMPLE AVERAGE) METHOD 
def simple_mean_forecast(data):
    return int(summition(data)/len(data))


# ============================================
# Mean Forecast Error (MFE)
# MFE = (actual_value - forcast) / number
# ============================================

def mean_forecast_error(data, forcast):
    actual_value = data[-2]
    mfe = (actual_value - forcast) / len(data)-1
    return mfe

# ============================================
# SIMPLE MOVING AVERAGE METHOD 
# ============================================

def simple_moving_average_forecast(data, startindex):
    if startindex > len(data) : 
        return "Error : please enter a stopindex greater than data length"
    else : 
        return int(summition(data[-startindex:]) / startindex)
    



# ============================================
# WEIGHTED MOVING AVERAGE METHOD 
# ============================================

def weighted_moving_average_forecast(data, weights):
    sum = 0
    actual_data = data[-len(weights):]
    forcast = []
    for i in range (1 ,len(weights)+1) :
        forcast.append(actual_data[-i] * weights[i-1])
        # print(actual_data[-i])
    # print (forcast)
    for i in forcast : 
        sum += i
    return int(sum)

# =============================================
# Exponential Smoothing Method
# forcast = alpha * actual_value + (1 - alpha) * (previous_forcast)
# =============================================

def exponential_smoothing_forecast(data, alpha):
    forcast = []
    forcast.append(300)
    for i in range(1, len(data)):
        new_forcast = data[i-1] * alpha + (1 - alpha) * forcast[i-1]
        forcast.append(new_forcast)
    # print("forcast : " + str(forcast))
    for i in range(len(forcast)):
        sum = 0
        sum += i
    return int(sum)

# ==============================================


# A THIRD EXPONENTIAL SMOOTHING
# forcast = alpha * actual_value + (1 - alpha) * (previous_forcast)
# ==============================================

def exponential_smoothing_forecast_3(data, alpha):
    forcast = []
    forcast.append(300)
    for i in range(1, len(data)):
        new_forcast = data[i-1] * alpha + (1 - alpha) * forcast[i-1]
        forcast.append(new_forcast)
    # print("forcast : " + str(forcast))
    for i in forcast:
        sum = 0
        sum += i
    return int(sum)

# ==============================================

# TREND PROJECTION
# ============================================== 

def trend_projection(data, b ,a):
    forcast = []
    forcast.append(300)
    for x in range(1, len(data)):
        new_forcast = x * b + a
        forcast.append(new_forcast)
    # print("forcast : " + str(forcast))
    return forcast[-1]
# ===============================================

print ("Naive Forecast: " + str(naive_forcast(data)))
print ("Simple Mean Forecast: " + str(simple_mean_forecast(data)))
print ("Mean Forecast Error : " + str(mean_forecast_error(data, simple_mean_forecast(data[0:-2]))))
print ("Simple Moving Average Forecast : " + str(simple_moving_average_forecast(data, 3)))
print ("Weighted Moving Average Forecast : " + str(weighted_moving_average_forecast(data, [0.5, 0.3, 0.2])))
print ("Exponential Smoothing Forecast : " + str(exponential_smoothing_forecast(data, 0.3)))
print ("Exponential Smoothing Forecast : " + str(exponential_smoothing_forecast_3(data, 0.3)))
print ("Trend Projection Forecast : " + str(trend_projection(data, 30, 295)))