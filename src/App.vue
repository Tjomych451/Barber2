<template>
  <div id="app" :style="customStyles">
    <CustomizationPanel />
    <!-- Your existing app content -->
  </div>
</template>

<script>
import CustomizationPanel from '@/components/CustomizationPanel.vue';
import { mapState } from 'vuex';

export default {
  components: {
    CustomizationPanel
  },
  computed: {
    ...mapState(['theme', 'layout', 'fonts']),
    customStyles() {
      return {
        '--primary-color': this.theme.primary,
        '--secondary-color': this.theme.secondary,
        '--accent-color': this.theme.accent,
        '--sidebar-width': this.layout.sidebarWidth,
        '--header-height': this.layout.headerHeight,
        '--font-primary': this.fonts.primary,
        '--font-secondary': this.fonts.secondary
      };
    }
  }
};
</script>
