<script setup lang="ts">
enum EventTypes {
  SUBMIT = 'submit'
}

const emit = defineEmits<{
  (event: EventTypes.SUBMIT): void
}>()

const props = defineProps<{
  title: string
}>()

const onSubmit = () => {
  emit(EventTypes.SUBMIT);
}
</script>

<template>
  <p class="text-3xl text-center">{{ props.title }}</p>

  <form @submit.prevent="onSubmit" class="flex flex-col pt-3 md:pt-8 max-w-xs">
    <slot name="fields"></slot>

    <slot name="actions"></slot>
  </form>

  <slot name="footer"></slot>
</template>
