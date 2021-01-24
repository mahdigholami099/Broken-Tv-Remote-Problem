controlNum = list(map(int, input().split()))
controlArr = list(map(int, input().split()))
tvChannelCost = []
for i in range(10):
    tvChannelCost.extend(list(map(int, input().split())))

origin, destination = input().split()
origin = int(origin)
destination = int(destination)

results = []

# check can go directly to destination with controlNum
if (destination > 9):
    if (controlArr[0] == 1):
        decimal = int((destination - (destination % 10))/10)
        if (controlNum[decimal] == 1) & (controlNum[destination % 10] == 1):
            results.append(3+tvChannelCost[origin]+tvChannelCost[destination])
elif controlNum[destination] == 1:
    results.append(1+tvChannelCost[origin]+tvChannelCost[destination])

## Combine points section
combinPoints = []
# Left far
for i in range(10):
    if controlNum[i] == 1:
        combinPoints.append(i)
        break
# Left close
decimal = None
if ((destination > 9) & controlArr[0] == 1) | (destination < 10):
    if controlNum[int(destination/10)] == 1:
        decimal = int(destination/10)
        for i in range((destination % 10)-1, -1, -1):
            if controlNum[i] == 1:
                combinPoints.append(decimal*10 + i)
                break
    else:
        for i in range(int(destination/10)-1, -1, -1):
            if controlNum[i] == 1:
                decimal = i
        for i in range(9, -1, -1):
            if controlNum[i] == 1:
                combinPoints.append(decimal*10 + i)
                break
else:
    for i in range(9, -1, -1):
        if controlNum[i] == 1:
            combinPoints.append(i)
            break

# Right far
for i in range(9,-1, -1):
    if controlNum[i] == 1:
        combinPoints.append(i*10 +i)
        break
# Right close
if ((destination > 9) & controlArr[0]==1) | (destination < 10):
    if controlNum[int(destination/10)] == 1:
        decimal = int(destination/10)
        for i in range(destination%10+1,10):
            if controlNum[i] == 1:
                combinPoints.append(decimal*10 + i)
                break
    else:
        for i in range(int(destination/10)+1,10):
            if controlNum[i] == 1:
                decimal = i
                break
        for i in range(10):
            if controlNum[i] == 1:
                combinPoints.append(decimal*10 + i)
                break
## End combin points section


# just with up arrow
def upArr(origin, destination):
    if origin < destination:
        return sum(tvChannelCost[i] for i in range(origin, destination+1)) + (destination-origin)
    else:
        score = sum(tvChannelCost[i]
                    for i in range(origin, len(tvChannelCost))) + (len(tvChannelCost) - origin)
        score += sum(tvChannelCost[i] for i in range(0, origin)) + origin
        return score

# just with down arrow
def downArr(origin, destination):
    if origin > destination:
        return sum(tvChannelCost[i] for i in range(destination, origin+1)) + (origin - destination)
    else:
        score = sum(tvChannelCost[i] for i in range(0, origin+1)) + origin + 1
        score += sum(tvChannelCost[i]
                     for i in range(destination, len(tvChannelCost))) + (len(tvChannelCost) - destination)
        return score

if controlArr[1] ==1:
    results.append(upArr(origin,destination))
    for cp in combinPoints:
            results.append(tvChannelCost[origin]+upArr(cp,destination) + 1 + (2*bool(cp>9)))
if controlArr[2] == 1:
    results.append(downArr(origin,destination))
    for cp in combinPoints:
            results.append(tvChannelCost[origin]+downArr(cp,destination) + 1 + (2*bool(cp>9)))

if results:
    print(min(results))
else:
    print('-1')
