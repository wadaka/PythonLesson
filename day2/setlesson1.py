scores={70,30,20,70}
scores.add(80)
scores.add(70)
print(scores)
print(len(scores))
print(sum(scores))

scores={'network':60,'database':80,'security':40}
members=['まつだ','だつま','つだま']
print(tuple(members))#('まつだ','だつま','つだま')
print(list(scores))#['network','database','security']
print(set(scores.values()))#{60,80}

matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={
        'まつだ':matsuda_scores,
        'あさぎ':asagi_scores,
        }
print(member_scores['まつだ']['network'])
        
member_hobbies={
        'まつだ':{'SNS','まあじゃん','自転車'},
        'あさぎ':{'まあじゃん','食べ歩き','数学','数学','数学'},
        }
print(member_hobbies)
print(member_hobbies['まつだ'])

common_hobbies=member_hobbies['まつだ']&member_hobbies['あさぎ']
print(common_hobbies)

a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
print(c[0])
print(c[1][2])

A={1,2,3,4}
B={2,3,4,5}
print(A|B) #{1,2,3,4,5}
print(A&B) #{2,3,4}
print(A-B) #{1}
print(A^B) #{1,4}
