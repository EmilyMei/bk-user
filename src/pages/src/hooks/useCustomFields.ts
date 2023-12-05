export const useCustomFields = (data, customFields) => {
  const result = Object.keys(data);
  const extras: any = [];
  customFields?.forEach((item) => {
    if (!result.includes(item.name)) {
      if (item.data_type === 'enum') {
        item.options.forEach((k: string) => {
          if (k.id === item.default) {
            extras.push({
              id: item.id,
              key: item.name,
              value: k.value,
            });
          }
        });
      } else if (item.data_type === 'multi_enum') {
        extras.push({
          id: item.id,
          key: item.name,
          value: item.options.filter((k: string) => item.default.includes(k.id)).filter(k => k.value),
        });
      } else {
        extras.push({
          id: item.id,
          key: item.name,
          value: item.default,
        });
      }
    } else {
      if (item.data_type === 'enum') {
        item.options.forEach((k: string) => {
          if (k.id === data[item.name]) {
            extras.push({
              id: item.id,
              key: item.name,
              value: k.value,
            });
          }
        });
      } else if (item.data_type === 'multi_enum') {
        extras.push({
          id: item.id,
          key: item.name,
          value: item.options.filter((k: string) => data[item.name].includes(k.id)).filter(k => k.value),
        });
      } else {
        extras.push({
          id: item.id,
          key: item.name,
          value: data[item.name],
        });
      }
    }
  });

  return extras;
};
