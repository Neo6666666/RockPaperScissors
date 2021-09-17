<template>
  <ul v-if="users.length">
    <li v-for="(user, i) in users" :key="user.id">
      <span>{{ i + 1 }} - {{ user.username }}</span>
      <span class="invite-button">+</span>
    </li>
  </ul>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  name: "UserList",
  setup() {
    const store = useStore();
    const { users } = store.state;

    return { users };
  },
});
</script>

<style scoped>
ul {
  list-style: none;
  display: block;
  max-width: 300px;
  width: 100%;
  margin: 20px auto 0 auto;
}

li {
  display: flex;
  background-color: white;
  box-shadow: 0px 0px 6px #0000002e;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 8px;
  justify-content: space-between;
  align-items: center;
}

.invite-button {
  padding: 5px 9px;
  color: white;
  background-color: #009000;
  border-radius: 50%;
  cursor: pointer;
}
</style>
