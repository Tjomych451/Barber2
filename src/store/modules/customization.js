import customizationConfig from '@/config/customization';

export default {
  state: {
    theme: customizationConfig.theme,
    layout: customizationConfig.layout,
    fonts: customizationConfig.fonts
  },
  mutations: {
    updateTheme(state, newTheme) {
      state.theme = { ...state.theme, ...newTheme };
    },
    updateLayout(state, newLayout) {
      state.layout = { ...state.layout, ...newLayout };
    },
    updateFonts(state, newFonts) {
      state.fonts = { ...state.fonts, ...newFonts };
    }
  }
};
