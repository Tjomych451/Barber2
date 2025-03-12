<template>
  <div class="customization-panel">
    <h3>Customize Your Interface</h3>
    <div class="color-picker">
      <label>Primary Color</label>
      <input type="color" v-model="theme.primary" @change="updateTheme">
    </div>
    <div class="layout-settings">
      <label>Sidebar Width</label>
      <input type="range" v-model="layout.sidebarWidth" @change="updateLayout">
    </div>
    <div class="font-settings">
      <label>Primary Font</label>
      <select v-model="fonts.primary" @change="updateFonts">
        <option value="Roboto">Roboto</option>
        <option value="Open Sans">Open Sans</option>
        <option value="Lato">Lato</option>
      </select>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'CustomizationPanel',
  computed: {
    ...mapState(['theme', 'layout', 'fonts'])
  },
  methods: {
    ...mapMutations(['updateTheme', 'updateLayout', 'updateFonts'])
  }
};
</script>
