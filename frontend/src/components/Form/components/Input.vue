<script setup lang="ts">
import { onUpdated } from '@vue/runtime-core'

enum EventTypes {
  INPUT = 'update:modelValue'
}

const emit = defineEmits<{
  (event: EventTypes.INPUT, newValue: string): void
}>()

const props = defineProps<{
  modelValue: string,
  placeholder: string,
  icon: string,
  type: string
}>()

const onInput = (event: Event) => {
  if (event.target) {
    emit(EventTypes.INPUT, (event.target as HTMLInputElement).value)
  }
}

onUpdated(() => console.log('updated'))
</script>

<template>
  <div class="flex relative">
    <span
      v-if="props.icon"
      class="inline-flex items-center px-3 border-t bg-white border-l border-b border-gray-300 text-gray-500 shadow-sm text-sm"
    >
      <img :src="props.icon" :alt="placeholder" />
    </span>

    <input
      @input="onInput"
      :value="props.modelValue"
      :type="props.type"
      :placeholder="placeholder"
      class="flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
    />
  </div>
</template>
