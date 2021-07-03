<template>
  <div class="home">
    <button v-on:click="sendMessage('hello')">Send Message</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  name: 'User',
  setup() {
    const user = JSON.parse(localStorage.getItem('user') || '');
    console.log(user)
    const connection = new WebSocket(`ws://localhost:8000/ws/${user.id}`);

    const sendMessage = message => {
        console.log("sendMessage")
        connection.send(message);
    }

    connection.onmessage = (event) => {
      console.log(event);
      console.log("onmessage Successfully connected to the echo websocket server...")
    }

    connection.onopen = (event) => {
      console.log(event)
      console.log("onopen Successfully connected to the echo websocket server...")
    }

    return { sendMessage }
  }
});
</script>
