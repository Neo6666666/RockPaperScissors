// import store from '@/store'

// enum messageStatus {
//   NEW_USER = 'NEW_USER',
//   ADD_USERS = 'ADD_USERS'
// }

export default class WebSocketService {
    socket: WebSocket
  
    constructor(id: string) {
      this.socket = new WebSocket(`ws://127.0.0.1:8000/users/?client_id=${id}`)
  
      this.open()
      this.onError()
      this.onClose()
    }
  
    open(): void {
      this.socket.onopen = () => {
        console.log('[open] Соединение установлено')
        console.log('Отправляем данные на сервер')
      }
    }
  
    onMessage(callback: (data: unknown) => void): void {
      this.socket.onmessage = (event: MessageEvent) => {
        console.log(`[message] Данные получены с сервера: ${event.data}`, typeof event)
  
        const data = JSON.parse(event.data)
  
        callback(data)
      }
    }
  
    onError(): void {
      this.socket.onerror = (error: unknown): void => {
        console.log(error)
      }
    }
  
    onClose(): void {
      this.socket.onclose = (e) => {
        if (e.wasClean) {
          console.log(
            `[close] Соединение закрыто чисто, код=${e.code} причина=${e.reason}`
          )
        } else {
          console.log('[close] Соединение прервано')
        }
      }
    }
  
    emit(payload): void {
      this.socket.send(JSON.stringify(payload))
    }
  }
  