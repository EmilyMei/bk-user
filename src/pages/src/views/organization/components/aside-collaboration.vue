<template>
  <section class="bg-white h-full pl-[6px]" v-bkloading="{ loading: loading }">
    <div class="leading-[36px] px-[6px] text-[#979BA5] text-[12px]">
      <span class="user-icon icon-tongbu pr-[4px]"></span>
      {{ $t('其他租户(通过跨租户协同分享)') }}
    </div>
    <div class="h-[calc(100%-36px)] overflow-y-auto">
      <div v-for="collaboration in collaborations" :key="collaboration.id">
        <collaboration-item :tenant="collaboration" />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';

import CollaborationItem from './collaboration-item.vue';

import { getCollaboration } from '@/http/organizationFiles';

const collaborations = ref([]);
const loading = ref(false);

onBeforeMount(async () => {
  loading.value = true;
  const tenantData = await getCollaboration();
  collaborations.value = tenantData?.data || [];
  loading.value = false;
});
</script>

