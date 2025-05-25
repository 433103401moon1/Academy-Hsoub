const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

const path = require("path");

module.exports = {
  mode: "development",
  entry: {
    app: "./src/index.js",
  },
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "main.js",
    clean: true,
    hotUpdateChunkFilename: "hot-update.js", // اسم ثابت لملف hot-update.js
    hotUpdateMainFilename: "hot-update.json", // اسم ثابت لملف hot-update.json
  },
  devServer: {
    static: {
      directory: path.join(__dirname, "public"),
    },
    port: 9000,
    hot: true,
    open: true,
    liveReload: true,
    watchFiles: ["src/**/*.html", "src/**/*.scss", "src/**/*.js", "src/**/*.css"],
    devMiddleware: {
      writeToDisk: true,
    },
  },
  module: {
    rules: [
      {
        test: /\.html$/i,
        loader: "html-loader",
        options: {
          minimize: false,
        },
      },
      // {
      //   test: /\.(sa|sc|c)ss$/,
      //   use: [
      //     MiniCssExtractPlugin.loader,
      //     "css-loader",
      //     {
      //       loader: "sass-loader",
      //       options: {
      //         sassOptions: {
      //           outputStyle: "compressed", // يزيل التعليقات عند الضغط
      //         },
      //       },
      //     },
      //   ],
      // },
      {
        test: /\.(sa|sc|c)ss$/i,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              esModule: false,
            },
          },
          "css-loader",
          "sass-loader"
        ],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: "asset/resource",
        generator: {
          filename: "./images/[name][ext]",
        },
      },
      {
        test: /\.(eot|svg|woff|woff2|ttf)$/i,
        type: "asset/resource",
        generator: {
          filename: "./fonts/[name][ext]",
        },
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: "index.html",
      template: "./src/index.html",
    }),
        new HtmlWebpackPlugin({
      filename: "product.html",
      template: "./src/product.html",
    }),
    new MiniCssExtractPlugin({
      filename: "css/style.css",
    }),
    new CssMinimizerPlugin(),
  ],
};
