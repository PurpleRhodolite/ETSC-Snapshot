const rupture = require("rupture");
const nib = require("nib");

module.exports = {
  pathPrefix: '/',
  siteMetadata: {
    title: 'Ethereum Social Network',
  },
  plugins: [
    'gatsby-plugin-react-helmet',
    {
      resolve: "gatsby-plugin-stylus",
      options: {
        use: [nib(), rupture()],
      },
    },
  ],
};
