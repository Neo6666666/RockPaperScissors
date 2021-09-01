<template>
  <div class="form__control form-input">
    <label class="form-input__label" for="username">
      {{ label }}
    </label>
    <input
      :value="modelValue"
      @input="handleInput"
      :name="inputName"
      :type="type"
      class="form-input__main"
    />
  </div>
</template>

<script lang="ts">
import { reactive, defineComponent } from "vue";

// type TState = { value: string };
// type TSetupState = { state: TState; handleChange: () => void };
// type TProps = {
//   label: string;
//   inputName: string;
//   value: string;
// };

export default defineComponent({
  name: "BaseInput",
  props: {
    label: String,
    type: String,
    inputName: String,
    modelValue: String,
  },
  emits: ["update:modelValue"],
  setup(props, { emit }) {
    const handleInput = (e: Event) => {
      const target = e.target as HTMLInputElement;

      console.log(e);

      emit("update:modelValue", target.value);
    };

    return { handleInput };
  },
});
</script>

<style></style>
