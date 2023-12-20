# 다섯 개의 문자열을 저장할 리스트를 생성합니다.
words = []

# 다섯 줄에 걸쳐서 문자열을 입력받아 리스트에 저장합니다.
for i in range(5):
    word = input().strip()  # 문자열을 입력받고 양쪽 공백을 제거합니다.
    words.append(word)

# 세로로 읽은 문자열을 저장할 변수를 생성합니다.
result = ""

# 다섯 개의 문자열 중 가장 긴 문자열의 길이를 구합니다.
max_len = max(len(word) for word in words)

# 가장 긴 문자열의 길이만큼 반복합니다.
for i in range(max_len):

    # 다섯 개의 문자열을 세로로 읽어서 result에 추가합니다.
    for j in range(5):

        # i번째 위치에 문자가 있으면 추가합니다.
        if i < len(words[j]):
            result += words[j][i]

# 세로로 읽은 문자열을 출력합니다.
print(result)