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

  open() {
    this.socket.onopen = (e) => {
      console.log("[open] Соединение установлено");
      console.log("Отправляем данные на сервер");
    };
  }

  message() {
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

  error() {
    this.socket.onerror = (error: any): void => {
      console.log(`[error] ${error?.message}`);
    };
  }

  close() {
    this.socket.onclose = (e) => {
      if (e.wasClean) {
        console.log(
          `[close] Соединение закрыто чисто, код=${e.code} причина=${e.reason}`
        );
      } else {
        // например, сервер убил процесс или сеть недоступна
        // обычно в этом случае event.code 1006
        console.log("[close] Соединение прервано");
      }
    };
  }

  send(message: string) {
    this.socket.send(JSON.stringify({ message, action: "select table drop" }));
  }

  // open – соединение установлено,
  // message – получены данные,
  // error – ошибка,
  // close – соединение закрыто.
}
