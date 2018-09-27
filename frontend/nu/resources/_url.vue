<template lang="html">
  <div class="">

    <section id="resource-table">
      <div class="container">
        <h1 class="text-center">Stay up to date</h1>
        <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <nav class="resource-options">
          <a href="#" class="active">Opción 1</a>
          <a href="#">Opción 2</a>
          <a href="#">Opción 3</a>
        </nav>
        <div class="table">
          <div class="top">
            <span>Ref.</span>
            <span>Category</span>
            <span>Price</span>
            <span>Link</span>
          </div>
          <div class="table-content" v-for="i in (0, 15)" :key="i">
            <span>Reference</span>
            <span>Category</span>
            <span>$19.99</span>
            <a href="#" target="_blank">Visit</a>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '~/assets/css/helpers/_variables.scss';
@import '~/assets/css/helpers/_mixins.scss';

#resource-table {
  padding: 70px 0 50px 0;
  background-color: $color-gray-light;
  h1 {
    margin: 0;
    padding: 0;
    margin-bottom: 30px;
  }
  .resource-options {
    display: flex;
    width: 100%;
    text-align: center;
    margin-bottom: 30px;
    a {
      flex: 1;
      text-decoration: none;
      font-family: $gotham-rounded-medium;
      color: $color-blue-black;
      border-bottom: 1px solid $color-gray;
      padding-bottom: 15px;
      font-size: 14px;
      &:hover {
        border-bottom: 3px solid $color-green;
      }
    }
    a.active {
      border-bottom: 3px solid $color-green;
    }
  }
  .table {
    display: block;
    width: 100%;
    .top, .table-content {
      display: flex;
      width: 100%;
      text-align: center;
      span,a {
        flex: 1;
        font-size: 14px;
      }
    }
    .top {
      background-color: $color-blue-heavy;
      padding: 15px 0;
      span {
        color: #fff;
      }
    }
    .table-content {
      background-color: #fff;
      border-bottom: 1px solid #adc7db;
      padding: 12px 0;
      span {
        color: $color-gray-heavy;
      }
      a {
        text-decoration: none;
        color: $color-green;
        font-family: $gotham-rounded-medium;
        &:hover {
          text-decoration: underline;
        }
      }
    }
  }
}
</style>
