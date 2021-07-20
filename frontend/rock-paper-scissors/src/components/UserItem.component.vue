<template>
  <li class="user-item">
    <div class="id">{{ user.id }}</div>
    <div class="username">{{ user.username }}</div>
    <div class="status">{{ user.status }}</div>
    <div class="invite" v-show="isInviteable">
      <input type="button" value="Invite" />
    </div>
  </li>
</template>

<script lang="ts">
import { computed, defineComponent, PropType } from "vue";
import { UserInterface } from "@/models/users/User.interface";

export default defineComponent({
  props: {
    user: Object as PropType<UserInterface>,
  },
  setup(props, { emit }) {
    const isInviteable = computed(() => {
      return props.user?.status === "Active";
    });

    return { isInviteable };
  },
});
</script>

<style>
.user-item {
  background: #363636;
  box-shadow: -10px -10px -10px rgba(255, 255, 255, 0.2),
    15px 15px 15px rgba(0, 0, 0, 0.1),
    inset -10px -10px -10px rgba(255, 255, 255, 0.2),
    inset 15px 15px 15px rgba(0, 0, 0, 0.1);
}
.username {
  color: white;
}
.invite {
  background: #363636;
  color: white;
  letter-spacing: 1px;
}
</style>
