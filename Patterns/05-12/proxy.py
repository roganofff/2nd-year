class UnauthorizedAccess(Exception):
    def __init__(self, room_name: str, user_name: str) -> None:
        super().__init__(f'User {user_name} tried to get access to Room {room_name}')

class Room:
    def __init__(self, name: str, access_groups: tuple[int], access_ids: tuple[int]) -> None:
        self.name, self.access_groups, self.access_ids = name, access_groups, access_ids
    
class User:
    def __init__(self, name: str, gid: int, uid: int, current_room: Room | None = None) -> None:
        self.name, self.gid, self.uid, self.current_room = name, gid, uid, current_room

class RoomAccess:
    def get(self, room: Room, user: User) -> None:
        if user.uid in room.access_ids or user.gid in room.access_groups:
            user.current_room = room
        else:
            raise UnauthorizedAccess(room.name, user.name)        

user = User('log', 12345, 11, Room('jjj', (12345, ), (11, )))
room = Room('Gostinnaya', (12345, ), (111, ))
print(user.current_room.name)
ra = RoomAccess()
ra.get(room, user)
print(user.current_room.name)