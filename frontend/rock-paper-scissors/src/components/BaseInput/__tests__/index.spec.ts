import { shallowMount } from "@vue/test-utils";
import BaseInput from "../index.vue";

describe("Base Input", () => {
  it("renders props.msg when passed", () => {
    const label = "new message";
    const wrapper = shallowMount(BaseInput, {
      props: { label },
    });
    expect(wrapper.text()).toMatch(label);
  });
});
