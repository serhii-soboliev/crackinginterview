class SmallestCommonRegion:

    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        super_regions = self.build_super_regions_dict(regions)
        super_regions1 = self.build_super_regions_hierarchy(super_regions[region1])
        super_regions1 = super_regions[region2]

    def build_super_regions_dict(self, regions):
        res = {}
        for region in regions:
            super_region = region[0]
            for subregion in regions[1:]:
                if res[subregion] is None:
                    res[subregion] = {super_region}
                else:
                    res[subregion].add(super_region)

    def build_super_regions_hierarchy(self, region, super_regions):
        res = set()
        current_super_regions = super_regions[region]
        while current_super_regions:
            for csr in current_super_regions:
                res.add(csr)

        return res
