<template>
  <base-input label="qweqwe" @handle-input="handleInput" :value="state.value" />
  <span>state.bar = {{ state.value }}</span>
</template>

<script lang="ts">
// import { useStore } from "vuex";
import { defineComponent, reactive } from "vue";
import baseInput from "@/components/BaseInput/index.vue";

export default defineComponent({
  name: "Login",
  components: {
    baseInput,
  },
  setup() {
    const state = reactive({ value: "" });
    const handleInput = (value: string) => {
      state.value = value;
    };

    return {
      state,

      handleInput,
    };
  },
});
</script>
