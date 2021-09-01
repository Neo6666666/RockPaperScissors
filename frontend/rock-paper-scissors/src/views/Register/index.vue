<template>
  <register-form @handle-submit="submitForm" />
</template>

<script lang="ts">
import { useStore } from "vuex";
import { defineComponent, reactive } from "vue";
import RegisterForm from "@/components/RegisterForm/index.vue";

export default defineComponent({
  name: "Login",
  components: {
    RegisterForm,
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

        store.dispatch("register", {
          username: user.username,
          password: user.password,
        });
      },
    };
  },
});
</script>
