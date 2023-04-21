# Django REST framwork API

### FK 이용한 참조
```
class ActorsDetailSerializer(serializers.ModelSerializer):
    movies = MoviesSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields= ['id','movies', 'name']    
    # 
    def to_representation(self, instance):
        represestation = super().to_representation(instance)
        represestation['movies'] = \
            [OD({'title' : od['title']}) for od in represestation['movies']]
        return represestation

```

- to_representation의 경우 instance가 모든 fields 를 반환
- instance 는 OrderedDict -> 딕셔너리를 하나의 인스턴스로 하는 리스트
- to_representation을 이용해 'movies'의 value를 'title'만으로 바꾸기 


