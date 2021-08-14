<template>
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

<style>
.sign-form-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3));
  width: 380px;
  padding: 50px 30px;
  border-radius: 10px;
  box-shadow: 7px 7px 60px black;
}
h3 {
  font-size: 2em;
  text-align: center;
  margin-bottom: 2em;
}
.form-control input {
  width: 100%;
  display: block;
  padding: 10px;
  color: #222;
  border: none;
  outline: none;
  margin: 1em 0em;
}
.form-control input[type="submit"] {
  background: rgb(34, 113, 216);
  color: white;
  text-transform: uppercase;
  font-size: 1.2em;
  opacity: 0.8;
}
</style>
