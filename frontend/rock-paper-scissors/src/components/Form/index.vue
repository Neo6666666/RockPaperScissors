<template>
  <div class="wrapper">
    <div class="sign-form-container">
      <h3>{{ title }}</h3>
      <form @submit.prevent="submitForm" class="sign-form">
        <base-input
          label="login"
          type="login"
          v-model:modelValue="state.username"
        />
        <base-input
          label="password"
          type="password"
          v-model:modelValue="state.password"
        />

        <button type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import BaseInput from "@/components/BaseInput/index.vue";

export default defineComponent({
  components: {
    BaseInput,
  },
  props: {
    title: String,
  },
  setup(props, { emit }) {
    const state: Record<string, string> = reactive({
      username: "",
      password: "",
    });

    return {
      state,

      submitForm() {
        emit("handle-submit", {
          username: state.username,
          password: state.password,
        });
      },
    };
  },
});
</script>

<style src="./styles/index.css"></style>
