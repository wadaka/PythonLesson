scores={'network':60,'database':80,'security':30}
print(scores)
print(scores['database'])
scores['asada']=43
scores['security']=55
print(scores)

del scores['asada']
print(scores)

total=sum(scores.values())
print(total)
