class Node:
    def __init__(self, data):
        self.data = data #노드가 저장하는 데이터
        self.next = None #다음 노드에 대한 래퍼런스(가리키는 역할)

    def __del__(self):
        self.a = 0
        #print("deleted")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find_node_at(self, index):
        #링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        #링크드 리스트 추가 연산 메소드
        new_node = Node(data)

        if self.head is None: #링크드 리스트가 비어있을때
            self.head = new_node
            self.tail = new_node
        else: #비어있지 않을때
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self) -> str:
        #링크드 리스트를 문자열로 표현하는 메소드
        res_str = "|"

        #링크드 리스트 안에 모든 노드를 돌기 위한 변수.
        #일단 가장 앞 노드로 정의
        iterator = self.head

        while iterator is not None:
            #각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str
            

#새로운 링크드 리스트 생성
new_list = LinkedList()

#링크드 리스트에 데이터 추가
new_list.append(2)
new_list.append(3)
new_list.append(5)
new_list.append(7)
new_list.append(11)

print(new_list)

#링크드 리스트 노드에 접근(데이터 가져오기)
print(new_list.find_node_at(3).data)

#링크드 리스트 노드에 접근(데이터 바꾸기)
new_list.find_node_at(2).data = 13

print(new_list)