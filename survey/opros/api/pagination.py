from rest_framework.pagination import PageNumberPagination


class PaginationOption(PageNumberPagination):
    page_size = 3