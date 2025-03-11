<script setup lang="ts">
import type { RadioGroupItemProps } from 'reka-ui'
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'
import { Check } from 'lucide-vue-next'
import {
  RadioGroupIndicator,
  RadioGroupItem,

  useForwardProps,
} from 'reka-ui'
import { computed } from 'vue'

const props = defineProps<RadioGroupItemProps & { class?: HTMLAttributes['class'] }>()

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props

  return delegated
})

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RadioGroupItem
    v-bind="forwardedProps"
    :class="
      cn(
        'peer aspect-square h-4 w-4 rounded-full border border-gray-200 border-gray-900 text-gray-900 shadow focus:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:cursor-not-allowed disabled:opacity-50 dark:border-gray-800 dark:border-gray-50 dark:text-gray-50 dark:focus-visible:ring-gray-300',
        props.class,
      )
    "
  >
    <RadioGroupIndicator class="flex items-center justify-center">
      <Check class="h-3.5 w-3.5 text-gray-900 dark:text-gray-50" />
    </RadioGroupIndicator>
  </RadioGroupItem>
</template>
