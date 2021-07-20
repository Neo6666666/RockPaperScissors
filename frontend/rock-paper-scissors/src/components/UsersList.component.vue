<template>
  <div class="user-list">
    <ul>
      <UserItem v-for="user in users" :key="user.id" :model="user" />
    </ul>
  </div>
</template>

<script lang="ts">
import UserItem from "./UserItem.component.vue";
import { UserInterface } from "@/models/users/User.interface";
import { defineComponent, PropType } from "@vue/runtime-core";

export default defineComponent({
  components: {
    UserItem,
  },
  props: {
    users: Array as PropType<UserInterface[]>,
  },
});
</script>

<style>
ul {
  list-style-type: none;
  margin-block-start: 0;
  margin-block-end: 0;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
}
</style>
