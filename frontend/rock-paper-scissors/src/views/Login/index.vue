<template>
  <login-form title="Login" @handle-submit="submitForm" />
</template>

<script lang="ts">
import { useStore } from "vuex";
import { defineComponent, reactive } from "vue";
import LoginForm from "@/components/LoginForm/index.vue";

export default defineComponent({
  name: "Login",
  components: {
    LoginForm,
  },
  setup() {
    const store = useStore();
    const state = reactive<{ value: string }>({ value: "" });
    const handleInput = (value: string) => {
      state.value = value;
    };

    return {
      state,

      handleInput,
      submitForm(user: { username: string; password: string }) {
        console.log(user);

        store.dispatch("login", {
          username: user.username,
          password: user.password,
        });
      },
    };
  },
});
</script>
