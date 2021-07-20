import store from "@/store";

export default class WebSocketService {
  socket: WebSocket;

  constructor(id: string) {
    this.socket = new WebSocket(`ws://127.0.0.1:8000/users/?client_id=${id}`);
  }

  open() {
    this.socket.onopen = (e) => {
      alert("[open] Соединение установлено");
      alert("Отправляем данные на сервер");
    };
  }

  message() {
    this.socket.onmessage = (event) => {
      alert(`[message] Данные получены с сервера: ${event.data}`);

      console.log("111111", store, JSON.parse(event.data));

      store.commit("setUsers", JSON.parse(event.data).users);
    };
  }

  error() {
    this.socket.onerror = (error: any): void => {
      alert(`[error] ${error?.message}`);
    };
  }

  close() {
    this.socket.onclose = (e) => {
      if (e.wasClean) {
        alert(
          `[close] Соединение закрыто чисто, код=${e.code} причина=${e.reason}`
        );
      } else {
        // например, сервер убил процесс или сеть недоступна
        // обычно в этом случае event.code 1006
        alert("[close] Соединение прервано");
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
