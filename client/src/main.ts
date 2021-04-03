import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";

createApp(App).use(store).mount("#app");

(async function () {
  await store.dispatch("loadSearchParams");
  await store.dispatch("refreshCourses", "?limit=100");
})();
