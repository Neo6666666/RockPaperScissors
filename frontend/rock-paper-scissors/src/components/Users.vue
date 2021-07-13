<template>
  <div class="home">
    <input type="text" name="test" v-model="message">
    <button v-on:click="sendMessage">Send Message</button>
    <UsersList :users="users"/>
    <template v-if="users.length">
      <ul>
        <li v-for="user in users" :key="user.id">{{user.username}}</li>
      </ul>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useStore, mapState } from 'vuex';

import UsersList from "./UsersList.component.vue";

import WebSocketService from '@/services/webSocket'

export default defineComponent({
  components: {
    UsersList
  },
  name: 'User',
  computed: {
    ...mapState({
      users: (state: any) => state.user.users
    })
  },
  setup() {
    const store = useStore();
    const user = JSON.parse(localStorage.getItem('user') || '');
    const users = store.state;
    const message = ref('');

    console.log('users', users);

    const connection = new WebSocketService(`${user.id}`);

    console.log( connection );
    

    connection.open()
    connection.message()
    connection.error()
    connection.close()

    const sendMessage = () => {
      // @ts-ignore
      console.log(typeof message, message);
      

      connection?.send(message.value);
    }

    return { message, sendMessage }
  }
});
</script>
