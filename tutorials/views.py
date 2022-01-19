from django.contrib.auth.models import User, Group
from rest_framework import mixins, viewsets, permissions, generics, renderers
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse

from tutorials.models import Snippet
from tutorials.permissions import IsOwnerOrReadOnly
from tutorials.serializers import UserSerializer, GroupSerializer, \
    UserSerializer, UserSerializerHyper, SnippetSerializerHyper


# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     # GET list of tutorials, POST a new tutorial, DELETE all tutorials
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
#
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
#
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
#                             status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     # find tutorial by pk (id)
#     try:
#         tutorial = Tutorial.objects.get(pk=pk)
#     except Tutorial.DoesNotExist:
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#         # GET / PUT / DELETE tutorial
#     tutorials = Tutorial.objects.filter(published=True)
#
#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#     elif request.method == 'PUT':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data)
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         tutorial.delete()
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def tutorial_list_published(request):
#     # GET all published tutorials
#     tutorials = Tutorial.objects.filter(published=True)
#
#     if request.method == 'GET':
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#
#
# class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, viewsets.ModelViewSet):
#     """
#     博客文章视图集
#
#     list:
#     返回博客文章列表
#
#     retrieve:
#     返回博客文章详情
#
#     list_comments:
#     返回博客文章下的评论列表
#
#     list_archive_dates:
#     返回博客文章归档日期列表
#     """
#     serializer_class = TutorialSerializer
#     queryset = Tutorial.objects.all()
#     # pagination_class = PageNumberPagination
#     pagination_class = LimitOffsetPagination
#     permission_classes = [AllowAny]
#
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_class = PostFilter
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return TutorialSerializer
#         elif self.action == 'retrieve':
#             return TutorialSerializer
#         else:
#             return super().get_serializer_class()

# @action(
#     methods=["GET"], detail=False, url_path="archive/dates", url_name="archive-date"
# )
# def list_archive_dates(self, request, *args, **kwargs):
#     dates = Post_rest.objects.dates("created_time", "month", order="DESC")
#     date_field = DateField()
#     data = [date_field.to_representation(date) for date in dates]
#     return Response(data=data, status=status.HTTP_200_OK)


# REST quickStart
class UserViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# 使用基于mixins 的混合试图构建SnippetList，减少代码重复


# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# # 使用通用的基于类的视图
# # 通过使用mixin类，我们使用更少的代码重写了这些视图，但我们还可以再进一步。REST框架提供了一组已经混合好（mixed-in）的通用视图，我们可以使用它来简化我们的views.py模块。
# class SnippetList1(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     pagination_class = LimitOffsetPagination
#     lookup_field = "title"
#
#
# class SnippetDetail1(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     pagination_class = LimitOffsetPagination
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer1
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer1


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


##REST框架包括一个用于处理ViewSets的抽象，它允许开发人员集中精力对API的状态和交互进行建模，并根据常规约定自动处理URL构造。

# ViewSet类与View类几乎相同，不同之处在于它们提供诸如read或update之类的操作，而不是get或put等方法处理程序。
#
# 最后一个ViewSet类只绑定到一组方法处理程序，当它被实例化成一组视图的时候，通常通过使用一个Router类来处理自己定义URL conf的复杂性。
#
# 使用ViewSets重构
# 我们看一下目前的视图，把它们重构成视图集。
#
# 首先让我们将UserList和UserDetail视图重构为一个UserViewSet
class UserViewSet1(viewsets.ReadOnlyModelViewSet):
    """此视图自动提供`list`和`detail`操作。"""
    queryset = User.objects.all()
    serializer_class = UserSerializerHyper


##接下来，我们将替换SnippetList，SnippetDetail和SnippetHighlight视图类。我们可以删除三个视图，并再次用一个类替换它们。
class SnippetViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    另外我们还提供了一个额外的`highlight`操作。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializerHyper
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @action(detail=True, methods=['GET'])
    def highlight(self, request, *args, **kwargs):
        snippt = self.get_object()
        return Response(snippt.highlight)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
