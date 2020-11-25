import pickle
profile_file = open("profile.pickle", "wb") # b for binary
profile = {"이름":"박명수", "나이":30, "취미":["축구","농구", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # store all data in profile in profile_file
profile_file.close()

profile_file = open("profile.pickle", "rb") 
profile = pickle.load(profile_file) # loads all data stored in profile.pickle
print(profile)
profile_file.close()