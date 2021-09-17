<template>
  <div class="home">
    <UsersList :users="users" @sendInvite="sendInvite" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore, mapState } from "vuex";

import UsersList from "./UsersList.vue";

import WebSocketService from "@/services/webSocket";

export default defineComponent({
  components: {
    UsersList,
  },
  name: "User",
  setup() {
    const user = JSON.parse(localStorage.getItem("user") || "");

    const connection = new WebSocketService(`${user.id}`);

    connection.open();
    connection.message();
    connection.error();
    connection.close();

    const sendInvite = () => {
      connection?.send({
        content_type: "INVITE_USER",
        host_id: 1,
        guest_id: 2,
      });
    };

    return { sendInvite };
  },
});
</script>

<style scoped>
input {
  max-width: 300px;
  width: 100%;
  height: 40px;
  margin: 20px auto 0 auto;
  display: block;
}

button {
  background-color: #0089ff;
  height: 40px;
  width: 100%;
  max-width: 300px;
  border: none;
  color: white;
  padding: 0 20px;
  display: block;
  font-size: 1.3em;
  margin: 0 auto;
}
</style>
