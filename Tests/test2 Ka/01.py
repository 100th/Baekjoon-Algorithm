def solution(string_list):
    userid = []
    nickname = []
    answer = []

    for i in range(len(string_list)):
        record_split = string_list[i].split()
        imci_id = record_split[1]

        if record_split[0] == "Enter":
            imci_nick = record_split[2]
            userid.append(imci_id)
            nickname.append(imci_nick)
            answer.append(imci_nick + "님이 들어왔습니다.")

        elif record_split[0] == "Change":
            imci_nick = record_split[2]
            index = userid.index(imci_id)
            nickname[index] = imci_nick

        elif record_split[0] == "Leave":
            userid.append(imci_id)
            index = userid.index(imci_id)
            imci_nick = nickname[index]
            answer.append(imci_nick + "님이 나갔습니다.")

        if imci_nick in nickname:
            index = userid.index(imci_id)
            nickname[index] = imci_nick

    return answer
