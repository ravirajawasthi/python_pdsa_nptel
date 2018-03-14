score_dict = {}
data = input()
while (data != ''):
    data = data.split(":")
    win = data[0]
    los = data[1]
    set_won = game_won = set_lose = set_win = 0
    scores = data[2].split(",")       
    if win not in score_dict.keys():  
        score_dict[win] = [0] * 6     
    if los not in score_dict.keys():  
        score_dict[los] = [0] * 6     
    if len(scores) > 3:               
        score_dict[win][0] += 1
    else:
        score_dict[win][1] += 1
    for score in scores:
        score = list(map(int,score.split("-")))
        if score[0] > score[1]:
            score_dict[win][2] += 1
            score_dict[los][4] += 1
        else:
            score_dict[los][2] += 1
            score_dict[win][4] += 1
        score_dict[win][3] += score[0]
        score_dict[win][5] += score[1]
        score_dict[los][5] += score[0]       
        score_dict[los][3] += score[1]
    data = input()    
temp = sorted(score_dict,key = lambda x: (score_dict[x][0],score_dict[x][1],score_dict[x][2],score_dict[x][3]), reverse = True)
for i in temp:
    print(i,end='')
    for j in score_dict[i]:
        print('',j,end='')
    print()    