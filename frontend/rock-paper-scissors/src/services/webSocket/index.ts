import store from "@/store";

enum messageStatus {
  NEW_USER = "NEW_USER",
  ADD_USERS = "ADD_USERS",
}

export default class WebSocketService {
  socket: WebSocket;

  constructor(id: string) {
    this.socket = new WebSocket(`ws://127.0.0.1:8000/users/?client_id=${id}`);
  }

  open(): void {
    this.socket.onopen = (e) => {
      console.log("[open] Соединение установлено");
      console.log("Отправляем данные на сервер");
    };
  }

  message(): void {
    this.socket.onmessage = (event: MessageEvent) => {
      console.log(
        `[message] Данные получены с сервера: ${event.data}`,
        typeof event
      );

      const eventData = JSON.parse(event.data);
      const response = {
        user: eventData.user,
        users: eventData.users,
        type: eventData.content_type,
      };

      if (response.type === messageStatus.ADD_USERS) {
        store.commit("setUsers", response.users);
      } else {
        store.commit("addUser", response.user);
      }
    };
  }

  error(): void {
    this.socket.onerror = (error: unknown): void => {
      console.log(error);
    };
  }

  close(): void {
    this.socket.onclose = (e) => {
      if (e.wasClean) {
        console.log(
          `[close] Соединение закрыто чисто, код=${e.code} причина=${e.reason}`
        );
      } else {
        console.log("[close] Соединение прервано");
      }
    };
  }

  send(message: string): void {
    this.socket.send(JSON.stringify({ message, action: "select table drop" }));
  }

  sendInvite() {}

  // open – соединение установлено,
  // message – получены данные,
  // error – ошибка,
  // close – соединение закрыто.
}
