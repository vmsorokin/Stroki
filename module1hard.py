grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
studets={'Johny', 'Bilbo','Steve','Khedrik','Aaron'}
print({
    sorted(studets)[0]:
        ((grades[0])[0]+(grades[0])[1]+(grades[0])[2]+(grades[0])[3]+(grades[0])[4])/len((grades[0])),
       sorted(studets)[1]:
           ((grades[1])[0]+(grades[1])[1]+(grades[1])[2]+(grades[1])[3])/len((grades[1])),
       sorted(studets)[2]:
           ((grades[2])[0]+(grades[2])[1]+(grades[2])[2]+(grades[2])[3])/len((grades[2])),
       sorted(studets)[3]:
           ((grades[3])[0]+(grades[3])[1]+(grades[3])[2])/len((grades[3])),
       sorted(studets)[4]:
           ((grades[4])[0]+(grades[4])[1]+(grades[4])[2]+(grades[4])[3]+(grades[4])[4])/len((grades[4])),
       })