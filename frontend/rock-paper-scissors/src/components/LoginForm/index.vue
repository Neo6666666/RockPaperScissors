<template>
  <base-form
    :title="title"
    @handle-submit="(user) => $emit('handleSubmit', user)"
  />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BaseForm from "@/components/Form/index.vue";

export default defineComponent({
  components: {
    BaseForm,
  },
  emits: ["handleSubmit"],
  props: {
    title: String,
  },
});
</script>
